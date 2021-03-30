
# coding: utf-8

# In[34]:


import pandas as pd


# In[35]:


def get_headers(dataframe):
    return dataframe.columns.values


# In[36]:


#Calculating mean 
def cal_mean(readings):
    sum_values = sum(readings)
    no = len(readings)
    mean = sum_values / float( no)
    return mean


# In[37]:


#Calculating variance
def cal_variance(readings):
    readings_mean = cal_mean(readings)
    mean_difference_squared_readings = [pow((reading - readings_mean), 2) for reading in readings]
    variance = sum(mean_difference_squared_readings)
    return variance / float(len(readings) - 1)


# In[38]:


#Calculating covariance
def cal_covariance(readings_1, readings_2):
    
    mean1 = cal_mean(readings_1)
    mean2 = cal_mean(readings_2)
    readings_size = len(readings_1)
    covariance = 0.0
    for i in range(0, readings_size):
        covariance += (readings_1[i] - mean1) * (readings_2[i] - mean2)
    return covariance / float(readings_size - 1)


# In[39]:


#Calculating wo and w1 in y=wo+w1x
def cal_simple_linear_regression_coefficients(x_readings, y_readings):
    w1 = cal_covariance(x_readings, y_readings) / float(cal_variance(x_readings))
    w0 = cal_mean(y_readings) - (w1 * cal_mean(x_readings))
    return w0, w1


# In[33]:


#Implementing Linear regression

def simple_linear_regression(dataset):
 
    
    dataset_headers = get_headers(dataset)
    print("Dataset Headers :: ", dataset_headers)
 
    
    square_feet_mean = cal_mean(dataset[dataset_headers[0]])
    price_mean = cal_mean(dataset[dataset_headers[1]])
 
    square_feet_variance = cal_variance(dataset[dataset_headers[0]])
    price_variance = cal_variance(dataset[dataset_headers[1]])
 
    
    
    covariance_of_price_and_square_feet = cal_covariance(dataset[dataset_headers[0]], dataset[dataset_headers[1]])
    w1 = covariance_of_price_and_square_feet / float(square_feet_variance)
 
    w0 = price_mean - (w1 * square_feet_mean)
 
  
    dataset['Predicted_Price'] = w0 + w1 * dataset[dataset_headers[0]]
    print(dataset)
 
 
if __name__ == "__main__":
 
    input_path =  r"C:\Users\Admin\Desktop\Job\Input_data.xlsx"
    house_price_dataset = pd.read_excel(input_path)
    simple_linear_regression(house_price_dataset)

