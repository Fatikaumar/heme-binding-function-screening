from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve
from matplotlib.ticker import MultipleLocator
import zipfile

root=Path(__file__).resolve().parents[1]
out=root/'figures'
out.mkdir(parents=True,exist_ok=True)

b=pd.read_csv(root/'results'/'blastp'/'blastp_top_matches.csv')
e=pd.read_csv(root/'results'/'esm2'/'esm2_top_matches.csv')
df=b.merge(e[['record_id','esm2_cosine_similarity']],on='record_id',validate='one_to_one')
assert len(df)==50 and df['record_id'].is_unique
assert set(df['dataset_group'])=={'AI_DESIGNED_POSITIVE','NATURAL_POSITIVE','NEGATIVE_CONTROL'}
assert (df['heme_binding_label'].str.lower()=='positive').sum()==30

navy='#17324d'; blue='#2A6092'; teal='#17817c'; gold='#df9252'; gray='#9aa5ad'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':15,'axes.labelsize':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

# FIG 1: All methods, curated from the run outputs (not all 50 raw scores are archived for these variants).
groups=['All 50 tests','AI-designed vs controls','Natural vs controls']
methods=[('BLASTp bit score',[.905,1.,.715],navy),('ESM-2 L6 mean',[.517,.512,.525],gray),('ESM-2 L6 CLS',[.542,.522,.580],gold),('ESM-2 L3 max',[.753,.802,.655],teal)]
fig,ax=plt.subplots(figsize=(11.5,6.7))
x=np.arange(len(groups)); width=0.19
for k,(name,values,color) in enumerate(methods):
 xpos=x+(k-1.5)*width
 bars=ax.bar(xpos,values,width*.95,label=name,color=color)
 for rect,val in zip(bars,values):
  ax.annotate(f'{val:.3f}',(rect.get_x()+rect.get_width()/2, val),xytext=(0,5),textcoords='offset points',ha='center',va='bottom',fontsize=8.2)
ax.axhline(.5,color='#b8c0c8',ls='--',lw=1,label='Chance-level ranking (0.5)')
ax.set_ylim(0,1.13);ax.set_ylabel('ROC AUC (higher = better separation)')
ax.set_xticks(x,groups);ax.yaxis.set_major_locator(MultipleLocator(.2))
ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
ax.set_title('Whole-protein screening: ranking performance',loc='left',pad=16,fontweight='bold',color=navy)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.12),ncol=3,frameon=False,fontsize=9)
fig.text(.06,.01,'Layer 3 max and Layer 6 CLS AUC values are from recorded Colab outputs; other values reproduced from original files.',fontsize=8.5,color='#5e6975')
fig.tight_layout(rect=[0,.035,1,1]);fig.savefig(out/'01_auc_comparison.png',dpi=180,bbox_inches='tight');plt.close(fig)

# FIG 2: BLAST matches based on exact E-value threshold.
group_order=[('AI-designed positives','AI_DESIGNED_POSITIVE'),('Natural positives','NATURAL_POSITIVE'),('Negative controls','NEGATIVE_CONTROL')]
sig=np.array([((df.dataset_group==g)&(df.evalue<=.01)).sum() for _,g in group_order])
total=np.array([(df.dataset_group==g).sum() for _,g in group_order])
fig,ax=plt.subplots(figsize=(10,5.5));y=np.arange(3)
ax.barh(y,sig,color=teal,label='E-value ≤ 0.01')
ax.barh(y,total-sig,left=sig,color='#dbe2e7',label='E-value > 0.01 / no hit')
for yi,(a,n) in enumerate(zip(sig,total)):
 ax.text(n+.25,yi,f'{a}/{n} significant',va='center',fontsize=10,color=navy)
ax.set_yticks(y,[g[0] for g in group_order]);ax.invert_yaxis()
ax.set_xlim(0,25);ax.set_xlabel('Number of test proteins');ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
ax.set_title('BLASTp: significant sequence matches',loc='left',fontweight='bold',color=navy,pad=14)
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.23),ncol=2,frameon=False)
fig.text(.08,.015,'Significant sequence alignment is not a heme-binding prediction.',fontsize=9,color='#5e6975')
fig.tight_layout(rect=[0,.035,1,1]);fig.savefig(out/'02_blastp_sequence_matches.png',dpi=180,bbox_inches='tight');plt.close(fig)

# Fig 3: overall ROC with original files
fig,ax=plt.subplots(figsize=(7.4,6.8))
for score,label,color in [('bitscore','BLASTp bit score',navy),('esm2_cosine_similarity','ESM-2 L6 mean',teal)]:
 y=(df.heme_binding_label=='positive').astype(int)
 fpr,tpr,_=roc_curve(y,df[score]); auc=roc_auc_score(y,df[score]);
 ax.plot(fpr,tpr,color=color,lw=2.4,label=f'{label} (AUC {auc:.3f})')
ax.plot([0,1],[0,1],'--',color='#b6bdc4',lw=1,label='Random ranking')
ax.set(xlim=(-.01,1.01),ylim=(-.01,1.04),xlabel='False-positive rate',ylabel='True-positive rate')
ax.set_title('ROC curves: all 50 test proteins',loc='left',color=navy,fontweight='bold',pad=12)
ax.grid(alpha=.2);ax.legend(loc='lower right',frameon=False)
fig.tight_layout();fig.savefig(out/'03_roc_all_proteins.png',dpi=180,bbox_inches='tight');plt.close(fig)

# Fig 4: natural positives vs negative ROC from original data
sub=df[df.dataset_group.isin(['NATURAL_POSITIVE','NEGATIVE_CONTROL'])]
fig,ax=plt.subplots(figsize=(7.4,6.8))
for score,label,color in [('bitscore','BLASTp bit score',navy),('esm2_cosine_similarity','ESM-2 L6 mean',teal)]:
 y=(sub.heme_binding_label=='positive').astype(int)
 fpr,tpr,_=roc_curve(y,sub[score]);auc=roc_auc_score(y,sub[score]);
 ax.plot(fpr,tpr,color=color,lw=2.4,label=f'{label} (AUC {auc:.3f})')
ax.plot([0,1],[0,1],'--',color='#b6bdc4',lw=1,label='Random ranking')
ax.set(xlim=(-.01,1.01),ylim=(-.01,1.04),xlabel='False-positive rate',ylabel='True-positive rate')
ax.set_title('ROC curves: natural positives vs controls',loc='left',color=navy,fontweight='bold',pad=12)
ax.grid(alpha=.2);ax.legend(loc='lower right',frameon=False)
fig.tight_layout();fig.savefig(out/'04_roc_natural_proteins.png',dpi=180,bbox_inches='tight');plt.close(fig)

# Fig 5: original mean pooled max cosine scores per protein group
fig,ax=plt.subplots(figsize=(9.5,5.5))
for j,(_,group) in enumerate(group_order):
 vals=df[df.dataset_group==group]['esm2_cosine_similarity'].values
 rng=np.random.default_rng(120+j); jitter=rng.uniform(-.14,.14,size=len(vals))
 ax.scatter(np.full(len(vals),j)+jitter,vals,alpha=.8,s=48,c=[blue,teal,gold][j],edgecolors='white',linewidth=.5)
 median=np.median(vals); ax.hlines(median,j-.25,j+.25,color=navy,lw=3)
 ax.text(j+.28,median,f'median {median:.3f}',fontsize=9,va='center',color=navy)
ax.set_xticks(range(3),[g[0] for g in group_order]);ax.set_ylabel('Top ESM-2 cosine similarity (Layer 6 mean)')
ax.set_ylim(.65,1.03);ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
ax.set_title('Overlap in ESM-2 similarity scores',loc='left',fontweight='bold',color=navy,pad=14)
fig.text(.1,.01,'Each dot is one test protein; horizontal bars indicate group medians.',fontsize=9,color='#5e6975')
fig.tight_layout(rect=[0,.03,1,1]);fig.savefig(out/'05_esm2_score_overlap.png',dpi=180,bbox_inches='tight');plt.close(fig)

