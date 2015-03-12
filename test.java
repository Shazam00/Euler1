private void Run() {
 
	int stop4=4;
	int stop6=6;
	double tot4=Math.Pow(stop4, 9);
	double tot6=Math.Pow(stop6, stop6);
 
	int[] a = new int[stop4*9+1];
	int[] b = new int[stop6*stop6+1];
 
	int[] majora = new int[a.Length];
	int[] majorb = new int[b.Length];
 
	// 4 side
	for (int i = 1; i <= stop4; i++) {
		for (int j = 1; j <= stop4; j++) {
			for (int h = 1; h <= stop4; h++) {
				for (int k = 1; k <= stop4; k++) {
					for (int x = 1; x <= stop4; x++) {
						for (int y = 1; y <= stop4; y++) {
							for (int z = 1; z <= stop4; z++) {
								for (int r = 1; r <= stop4; r++) {
									for (int s = 1; s <= stop4; s++) {
										int sum=i+j+h+k+x+y+z+r+s;
										a[sum]++;
									}
								}
							}
						}
					}
				}
			}
		}
	}
 
	// 6 side
	for (int i = 1; i <= stop6; i++) {
		for (int j = 1; j <= stop6; j++) {
			for (int h = 1; h <= stop6; h++) {
				for (int k = 1; k <= stop6; k++) {
					for (int x = 1; x <= stop6; x++) {
						for (int y = 1; y <= stop6; y++) {
							int sum=i+j+h+k+x+y;
							b[sum]++;
						}
					}
				}
			}
		}
	}
 
 
	// parse arrays
	for (int i = a.Length-1; i >0; i--) {
		majora[i-1]=majora[i]+a[i];
	}
 
	for (int i = b.Length-1; i >0; i--) {
		majorb[i-1]=majorb[i]+b[i];
	}
 
	double proba=0, probb=0, probc=0;
 
	for (int i = 0; i < a.Length; i++) {
		double x=(double)majora[i];
		double y=(double)b[i];
		proba += x*y;
	}
	proba/=(tot4*tot6);
 
	for (int i = 0; i < a.Length; i++) {
		double x=(double)majorb[i];
		double y=(double)a[i];
		probb += x*y;
	}
	probb/=(tot4*tot6);
 
	for (int i = 0; i < a.Length; i++) {
		double x=(double)a[i];
		double y=(double)b[i];
		probc += x*y;
	}
	probc/=(tot4*tot6);
 
	Console.WriteLine("tot4 = {0}, tot6 = {1}", tot4, tot6);
	Console.WriteLine("Probability a is: {0}", proba);
	Console.WriteLine("Probability b is: {0}", probb);
	Console.WriteLine("Probability c is: {0}", probc);
	Console.WriteLine("Probability a+b+c is: {0}", proba + probb + probc);
}