import json,os,time
from urllib.request import urlopen as U,Request
P='PNBRQK';W=(100,320,330,500,900,0)
N=(-21,-19,-12,-8,8,12,19,21);B=(-11,-9,9,11);R=(-10,-1,1,10);K=B+R
Z=((25,27,1,(25,26,27),0),(25,23,2,(25,24,23),0),(95,97,4,(95,96,97),1),(95,93,8,(95,94,93),1))
def a(b,s,w):
 q=('p','P')[w];d=9 if w else -9
 if q in (b[s-d],b[s-d-2*(1 if w else -1)]):return 1
 for ds,pc in ((N,'N'),(K,'K')):
  q=(pc.lower(),pc)[w]
  for x in ds:
   if b[s+x]==q:return 1
 for ds,pc in ((B,'B'),(R,'R')):
  z=(pc.lower()+'q',pc+'Q')[w]
  for x in ds:
   t=s+x
   while b[t]=='.':t+=x
   if b[t] in z:return 1
 return 0
def g(b,w,c,e):
 m=[]
 for s in range(21,99):
  p=b[s]
  if p<'A' or p.isupper()!=w:continue
  u=p.upper()
  if u=='P':
   d=10 if w else -10;z=[s+d] if b[s+d]=='.' else []
   if z and (s//10==3 if w else s//10==8) and b[s+2*d]=='.':z.append(s+2*d)
   z+=[s+o for o in (d-1,d+1) if s+o==e or b[s+o] not in ' .Kk' and b[s+o].isupper()!=w]
   for t in z:m+=[(s,t,q) for q in (('qrbn','QRBN')[w] if (t>90 if w else t<29) else ('',))]
  else:
   for d in (N,K,B,R,B+R)['NKBRQ'.index(u)]:
    t=s+d
    while b[t]=='.' or b[t] not in ' .Kk' and b[t].isupper()!=w:
     m.append((s,t,''))
     if b[t]!='.' or u not in 'BRQ':break
     t+=d
   if u=='K':
    for f2,t2,bi,pa,by in Z:
     if s==f2 and c&bi and all(b[x]=='.' for x in pa[1:]+((f2-3,) if t2<f2 else ())) and not any(a(b,x,by) for x in pa):m.append((f2,t2,''))
 return m
def y(s,m):
 b,w,c,e=s;f,t,q=m;L=list(b);o=L[f];L[t]=q or o;L[f]='.'
 if t==e and o in 'Pp':L[t-10 if o=='P' else t+10]='.'
 if o in 'Kk' and abs(t-f)==2:
  v=t+1 if t>f else t-2;L[v]='.';L[t-1 if t>f else t+1]='Rr'[o=='k']
 if o in 'Kk':c&=(3,12)[o=='K']
 for x,z in ((28,14),(21,13),(98,11),(91,7)):
  if f==x or t==x:c&=z
 return (''.join(L),not w,c,(f+t)//2 if o in 'Pp' and abs(t-f)==20 else 0)
def l(s,q=0):
 b,w,c,e=s;r=[]
 for m in g(b,w,c,e):
  if q and b[m[1]]=='.' and not m[2] and m[1]!=e:continue
  t=y(s,m);d=t[0];k=m[1] if b[m[0]] in 'Kk' else d.index('K' if w else 'k')
  if not a(d,k,not w):r.append((m,t))
 return r
def v(b,w):
 s=0
 for i,p in enumerate(b):
  if p<'A':continue
  u=p.upper();k=P.index(u);f=i%10-1;r=i//10-2;n=14-abs(2*f-7)-abs(2*r-7);z=r if (q:=p.isupper()) else 7-r
  x=W[k]+(6*z if u=='P' else 0)+(1,3,3,2,1,-2)[k]*n
  s+=x if q else -x
 return s if w else -s
G=[0];NB=60000;M=10**5
class E(Exception):pass
def o(m,b):return (W[P.index(b[m[1]].upper())] if b[m[1]]!='.' else 0)*10-W[P.index(b[m[0]].upper())]//32+900*bool(m[2])
def r(s,d,u,e):
 b,w,c,f=s;G[0]+=1
 if G[0]>NB:raise E
 if d<=0:
  n=v(b,w)
  if n>=e:return e
  if n>u:u=n
  for m,t in sorted(l(s,1),key=lambda x:o(x[0],b),reverse=True)[:1]:
   n=-r(t,0,-e,-u)
   if n>=e:return e
   if n>u:u=n
  return u
 ms=l(s)
 if not ms:return -M if a(b,b.index('K' if w else 'k'),not w) else 0
 for m,t in sorted(ms,key=lambda x:o(x[0],b),reverse=True):
  n=-r(t,d-1,-e,-u)
  if n>=e:return e
  if n>u:u=n
 return u
def h(s):
 G[0]=0;z=None;ms=l(s)
 if not ms:return None
 for d in range(1,7):
  try:z=max(ms,key=lambda x:-r(x[1],d-1,-M,M))[0]
  except E:break
 return z
def n(m):return '%c%d%c%d%s'%(m[0]%10+96,m[0]//10-1,m[1]%10+96,m[1]//10-1,m[2].lower())
def F(f):
 t=f.split();L=list(' '*20+' ........ '*8+' '*20);i=91
 for ch in t[0]:
  if ch=='/':i-=18
  elif ch.isdigit():i+=int(ch)
  else:L[i]=ch;i+=1
 c=sum(1<<'KQkq'.index(c) for c in t[2] if c in 'KQkq')
 return (''.join(L),t[1]=='w',c,21+ord(t[3][0])-97+(int(t[3][1])-1)*10 if t[3]!='-' else 0)
def Q(p,b):
 try:
  q=Request(u+p,data=json.dumps(b).encode())
  r=json.loads(U(q,timeout=10).read())
  return r if type(r) is dict else {}
 except Exception:return {}
u=os.environ.get('MAKEFUN_ENV_URL')
if u:
 while 1:
  d=Q('/game',{});s=d.get('status');J=d.get('game')
  if s=='done':break
  if s!='your_move':time.sleep(1);continue
  while s=='your_move':
   try:m=n(h(F(d['fen'])))
   except Exception:m=None
   if not m:Q('/resign',{'game':J});break
   if m not in (d.get('legal_moves') or [m]):m=d['legal_moves'][0]
   d=Q('/move',{'game':J,'move':m});s=d.get('status')
