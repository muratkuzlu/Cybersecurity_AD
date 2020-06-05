
import random
def add_noise(x, y, sigma, mu, percent):
    #sigma=50
    #mu=10
    #percent=.10

    y_noise=pd.DataFrame(data=y, index=y.index)
    num=int(percent*len(y))
    noise = np.random.normal(mu, sigma, [num,]) 
    #x_test_noise=pd.DataFrame(x_test)
    noise_sample=y.sample(n=num,replace=False, axis=0) * (1+ (noise/100))
    for i in  noise_sample.index:
        y_noise.iloc[i]=noise_sample.loc[i]
    return(y_noise)
                
# the function assumes x and y to be scaled and y to be a pandas series 

noisy_y = add_noise(x, y)
