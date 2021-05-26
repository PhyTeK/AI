/* Simple neural network in C */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NIN 2
#define NHID 2
#define NOUT 1
#define NTRA 4
#define NEPO 10000
#define LR 0.5 // Learning rate

// Functions declarations
double init_wb(void); // Init weigths and biases
void shuffle(int*,int);
double sigmoid(double);
double dSigmoid(double);

// Activation function and its derivative
double sigmoid(double x) { return 1/(1 + exp(-x)); }
double dSigmoid(double x) { return x*(1-x); }

double init_wb(void){ return ((double)rand())/((double)RAND_MAX);}
  
void shuffle(int*a,int n){
  // Switch randomly two elements of a
  int i,m,p,t;
  
  for(i=0;i<n;i++){
    p = n*(double)rand()/(double)RAND_MAX;
    m = n*(double)rand()/(double)RAND_MAX;
    t = a[p];
    a[p] = a[m];
    a[m] = t;
  }
}

int main(){
  FILE *fout;
  int i,j,k,n,x,q;
  int epochs = NEPO;
  
  double lr = LR; // learning rate
  double activ,derr;
  double delhid[NHID], delout[NOUT];
  
  double hlayer[NHID];
  double olayer[NOUT];

  double hlbias[NHID];
  double olbias[NOUT];

  double hweight[NIN][NHID];
  double oweight[NHID][NOUT];
  

  double train_in[NTRA][NIN] =
    {{0.0f,0.0f},{1.0f,0.0f},{0.0f,1.0f},{1.0f,1.0f}};

  double train_out[NTRA][NOUT] =
    {{0.0f},{1.0f},{1.0f},{0.0f}};

  
  // Iterate through the entire training for a number of epochs
  int train_order[NTRA] = {0,1,2,3};

  // Init all weights and biases between 0.0 and 1.0
  for (i=0;i<NHID;i++)
    hlbias[i] = init_wb();
  for(i=0;i<NOUT;i++)
    olbias[i] = init_wb();
  for(i=0;i<NIN;i++)
    for(j=0;j<NHID;j++)
      hweight[i][j] = init_wb();
  for(i=0;i<NHID;i++)
    for(j=0;j<NOUT;j++)
      oweight[i][j] = init_wb();

  fout = fopen("nnerr.txt","w");
  
  for(n=0;n<epochs;n++){
    // As per SGD, shuffle the order of the training set

    shuffle(train_order,NTRA);
    
    // Cycle through each of the training set elements
    for (x=0; x<NTRA; x++) {
      i = train_order[x];
  
      // Compute hidden layer activation
      for (j=0; j<NHID; j++) {
	activ = hlbias[j];

	for (k=0; k<NIN;k++) {
	  activ += train_in[i][k]*hweight[k][j];
	}
	
	hlayer[j] = sigmoid(activ);
      }

      // Compute output layer activation
      for(j=0; j<NOUT;j++) {
	activ = olbias[j];

	for(k=0; k<NHID;k++) {
	  activ += hlayer[k]*oweight[k][j];
	}
	
	olayer[j] = sigmoid(activ);
      }

      // Compute change in output weights
      for(j=0; j<NOUT;j++) {
	derr = (train_out[i][j]-olayer[j]);
	// Print error
	if(n%10)
	  fprintf(fout,"%f\n",derr);

	delout[j] = derr*dSigmoid(olayer[j]);	
      }
  
      // Compute change in hidden weights
      for(j=0; j<NHID; j++) {
	derr = 0.0f;
	for(k=0; k<NOUT; k++) {
	  derr += delout[k]*oweight[j][k];
	}
	delhid[j] = derr*dSigmoid(hlayer[j]);
      }
  
      // Apply change in output weights
      for (j=0; j<NOUT; j++) {
	olbias[j] += delout[j]*lr;
	for (k=0; k<NHID; k++) {
	  oweight[k][j] += hlayer[k]*delout[j]*lr;
	}
      }
      // Apply change in hidden weights
      for (j=0; j<NHID;j++) {
	hlbias[j] += delhid[j]*lr;
	for(k=0; k<NIN; k++) {
	  hweight[k][j] += train_in[i][k]*delhid[j]*lr;
	}
      }
    }
  }

  fclose(fout);
  
  return 0;
}
