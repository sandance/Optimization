import java.io.*;
import java.util.*;

public class LIS_Solution {

		public static int LCS(int [] arr) {
			int [] L = new int [arr.length];
			
			for(int i=0; i < L.length; i++ ) 
					L[i]=1;

			 
			
			for (int i =1; i < L.length; i++){
				//int maxn = 0;
				
				for(int j=0; j<i; j++){
					if(arr[i] > arr[j] && L[i] <  L[j] +1 ) {
						L[i] = L[j] +1 ;
					}
				}
				//L[i] = maxn + 1;
			}
			
			for(int i=0;i< L.length; i++) 
				System.out.println(L[i]);

			
			int maxi = 0;
			
			for(int i=0; i < L.length; i++)
			{
				if ( L[i] > maxi) {
					maxi = L[i];
				}
			}

			return maxi;
		}

		public static void main(String[] args) throws IOException {
				Scanner in = new Scanner(System.in);
				PrintWriter out = new PrintWriter(System.out);

				System.out.println("enter number of elements\n");
				int n = in.nextInt();

				// dynamically allocate array and store array values
				int [] arr= new int[n];
			
				for(int i=0;i<n;i++)
					arr[i] = in.nextInt();

				int max = LCS(arr);
			
				System.out.println("Longest Increating Subsequence\t" + max );
		}

}
