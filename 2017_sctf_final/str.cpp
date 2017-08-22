#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
using namespace std;
#define MAXX 130123
int group[MAXX],newgroup[MAXX],SA[MAXX],lcp[MAXX], map[MAXX];

char S[MAXX];
char final[MAXX];
char final_tp[MAXX];
int N,t;
void getSA();

void getLCP();

bool cmp(int i, int j)
{
    if(group[i] != group[j])
        return group[i]<group[j];
    return group[i+t]<group[j+t];
}
int main()
{
	cin.getline(S, MAXX);
    //scanf("%s",S);
    
    N=strlen(S);
    
    getSA();
    getLCP();
    int maxx=0;
    for(int a=0; a<N; a++)
    {
    	//printf("%d\n", lcp[a]);
    	if(lcp[a] > maxx){
    		maxx = lcp[a];
    		sprintf(final, "%.*s", maxx, S+map[a]);
        	//printf("update: %s\n", final);
		}
		else if(lcp[a] == maxx){
			sprintf(final_tp, "%.*s", maxx, S+map[a]);
			//printf("same: %s %s\n", final, final_tp);
			if(strcmp(final, final_tp) > 0){
				strcpy(final, final_tp);
			}
		}
    }
    printf("%s", final);
    // printf("%d\n",maxx);
}

void getSA()
{
    for(int a=0; a<N; a++)
    {
        group[a]=S[a];
        SA[a]=a;
    }
    t=1;
    group[N]=-1;
    newgroup[N]=-1;
    while(t<N)
    {
        sort(SA,SA+N,cmp);
        
        for(int a=0; a<N; a++)
        {
            if(cmp(SA[a-1],SA[a]))
                newgroup[a]=newgroup[a-1]+1;
            else
                newgroup[a]=newgroup[a-1];
        }
        
        for(int a=0; a<N; a++)
        {
            group[SA[a]]=newgroup[a];
        }
        t*=2;
        if(t>N)
            break;
    }
   // for(int a=0; a<N; a++)
    //{
     //   printf("%d %d %d\n",SA[a],group[a],newgroup[a]);
   // }
}

void getLCP()
{
    for(int a=0,k=0; a<N; a++)
    {
        if(group[a]==0)
            lcp[group[a]]=0;
        else{
        for(int j=SA[group[a]-1]; S[a+k]==S[j+k]; k++);
        
        lcp[group[a]]=k;
        map[group[a]]=a;
        
        if(k)
            k--;
        }
    }
}
