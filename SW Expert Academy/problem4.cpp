#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
const int MAX_NUM = 2147483647;

int solution(int n, int k){
    vector<vector<int> > arr(k, vector<int>(n,0));
    vector<vector<int> > dist(k, vector<int>(n,0));
    vector<pair<int,int> > ones;
    
    for(int r=0;r<k;r++){
        string line;
        cin >> line;
        for(int c=0;c<n;c++){
            arr[r][c] = line[c]-'0';
            if(arr[r][c]==1){
                ones.push_back(make_pair(r,c));
            }
            dist[r][c] = MAX_NUM;
        }
    }
    for(int i=0;i<ones.size();i++){
        int r = ones[i].first;
        int c = ones[i].second;
        dist[r][c] = 0;
        
        for(int j=1;j<=k/2;j++){
            if(arr[(r+j)%k][c]==1){
                break;
            }else{
                dist[(r+j)%k][c] = min(dist[(r+j)%k][c], j);
            }
        }
        for(int j=1;j<=k/2;j++){
            if(arr[(r-j+k)%k][c]==1){
                break;
            }else{
                dist[(r-j+k)%k][c] = min(dist[(r-j+k)%k][c], j);
            }
        }
    }
    
    int min_num = MAX_NUM;
    for(int r=0;r<k;r++){
        int sum = 0;
        for(int c=0;c<n;c++){
            sum += dist[r][c];
        }
        min_num = min(sum,min_num);
    }
    return min_num;
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    int tc;
    cin >> tc;
    
    for(int i=0;i<tc;i++){
        int n,k;
        cin >> n >> k;
        cout << "#" << i+1 << " " << solution(n,k) << endl;
    }
    
    return 0;
}
