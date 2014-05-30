import java.io.*;
import java.util.*;


public class lcs_solution {

			public static int lcs(String a,String b, int m,int n){
					// Array to store results
					int [][] L = new int[m+1][n+1];
				
					/* Following steps going to build L[m+1][n+1] in bottom up fashion */
					
					for(int i=0;i<=m;i++){
						for(int j=0;j<=n;j++){
							if ( i==0 || j==0)
								L[i][j] = 0;
							else if (a.charAt(i-1) == b.charAt(j-1))
								L[i][j] = L[i-1][j-1] +1;
							else
								L[i][j] = Math.max(L[i-1][j], L[i][j-1]);
						}
					}
			
					for(int i=0; i<=m;i++)
							for (int j=0;j<=n;j++){
								System.out.print(L[i][j]);
								if (j==n)
									System.out.println("\n");
							}
					return L[m][n];

					
			}
		
			public static void main(String[]  args) throws IOException {
					BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
					System.out.println("Enter First String\n");
					String fst = br.readLine();

					System.out.println("Enter Second String\n");
					String snd = br.readLine();
					System.out.println("M value " + fst.length() + "N value" + snd.length());
					
					int  result = lcs(fst,snd,fst.length(),snd.length());
					
					System.out.println("Longest common Subsequence is : \t" + result);
					//System.out.println("Length of Subsequence is: \t " + result.length() );
				
			}
}
					
			
