#include <iostream>
#define ARRAYSIZE(A) sizeof(A)/sizeof((A)[0])
 
int array_max(int a[], int size) {
    int max = a[0];
    for(int i=1; i<size; i++) if(a[i]>max) max=a[i];
    return max;
}
 
using namespace std;
int main()
{
    int T,M;
    int Arr[10];
    cin >> T;
     
    for(int i = 0; i < T; i++){
        for(int i = 0; i < 10; i++) cin >> Arr[i];
        int size = ARRAYSIZE(Arr);
        int max = array_max(Arr, size);
        cout << "#" << i+1 << " "<<max << "\n"; 
    }
}