import java.io.*;
import java.util.*;

public class edit_distance {
			public static int  edit_distance_dp(String a , String b, int m, int n) {
				// Here m and n are the length of String a and String b
				int [][] L = new int [m+1][n+1];

				for(int i=0;i<m;i++)
						L[i][0] = i;

				for(int j=0;j<n;j++)
						L[0][j] = j;


				// Now iterate through both loops

				for(int i=0;i<m;i++){
					char c1 = a.charAt(i);
					for(int j=0;j<n;j++){
						char c2= b.charAt(j);

						if(c1==c2){
							// no edit cost
							L[i+1][j+1]=L[i][j]; // Keep diagonal value in matrix
						}
						else {

							int replace = 1 + L[i][j]; // Add 1 to its current value
							int delete = L[i][j+1] + 1;
							int insert = L[i+1][j] +1; 

							int min = replace > insert ? insert : replace;
	
							min = delete > min ? min : delete;
							
							L[i+1][j+1] = min;
						}			
					}
				}	
				return L[m][n];	
			
			}	
			public static void main(String[] args) throws IOException {
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				System.out.println("Enter the first string\n");
				String a = br.readLine();
				System.out.println("Enter the Second string\n");
				String b = br.readLine();
				
				// Calling edit_distance_dp function to calculate min edit distance value 

				int result = edit_distance_dp(a,b,a.length(),b.length());

				System.out.println("Minimum number of steps to convert string 1 to string b is:\t" + result);
			}
}
