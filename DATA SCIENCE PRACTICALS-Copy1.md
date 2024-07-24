```python
#EXPERIMENT 1
import pandas as pd
# Load file
df= pd.read_csv('DATA_SCIENCE_DATASET.csv')
print(df.head())
```

       StudentID  Age  Gender  Ethnicity  ParentalEducation  StudyTimeWeekly  \
    0       1001   17       1          0                  2        19.833723   
    1       1002   18       0          0                  1        15.408756   
    2       1003   15       0          2                  3         4.210570   
    3       1004   17       1          0                  3        10.028829   
    4       1005   17       1          0                  2         4.672495   
    
       Absences  Tutoring  ParentalSupport  Extracurricular  Sports  Music  \
    0         7         1                2                0       0      1   
    1         0         0                1                0       0      0   
    2        26         0                2                0       0      0   
    3        14         0                3                1       0      0   
    4        17         1                3                0       0      0   
    
       Volunteering       GPA  GradeClass  
    0             0  2.929196         2.0  
    1             0  3.042915         1.0  
    2             0  0.112602         4.0  
    3             0  2.054218         3.0  
    4             0  1.288061         4.0  
    


```python
import pandas as pd
#loading 2nd dataset
df1=pd.read_csv('Mall_Customers.csv')
print(df1.head())
```

       CustomerID   Genre  Age  Annual Income (k$)  Spending Score (1-100)
    0           1    Male   19                  15                      39
    1           2    Male   21                  15                      81
    2           3  Female   20                  16                       6
    3           4  Female   23                  16                      77
    4           5  Female   31                  17                      40
    


```python
df2=pd.concat([df,df1],axis=1)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>StudentID</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Ethnicity</th>
      <th>ParentalEducation</th>
      <th>StudyTimeWeekly</th>
      <th>Absences</th>
      <th>Tutoring</th>
      <th>ParentalSupport</th>
      <th>Extracurricular</th>
      <th>Sports</th>
      <th>Music</th>
      <th>Volunteering</th>
      <th>GPA</th>
      <th>GradeClass</th>
      <th>CustomerID</th>
      <th>Genre</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>19.833723</td>
      <td>7</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2.929196</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>Male</td>
      <td>19.0</td>
      <td>15.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>15.408756</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.042915</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>Male</td>
      <td>21.0</td>
      <td>15.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>15</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>4.210570</td>
      <td>26</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.112602</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>Female</td>
      <td>20.0</td>
      <td>16.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>10.028829</td>
      <td>14</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2.054218</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>Female</td>
      <td>23.0</td>
      <td>16.0</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>4.672495</td>
      <td>17</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.288061</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>Female</td>
      <td>31.0</td>
      <td>17.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2387</th>
      <td>3388</td>
      <td>18</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>10.680555</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.455509</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2388</th>
      <td>3389</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.583217</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>3.279150</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2389</th>
      <td>3390</td>
      <td>16</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>6.805500</td>
      <td>20</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1.142333</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2390</th>
      <td>3391</td>
      <td>16</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>12.416653</td>
      <td>17</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1.803297</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2391</th>
      <td>3392</td>
      <td>16</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>17.819907</td>
      <td>13</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2.140014</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2392 rows × 20 columns</p>
</div>




```python

```


```python

```
