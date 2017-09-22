


<h1>Heroes of Pymoli Data Analysis</h1>
<img src="http://fantasy-faction.com/wp-content/uploads/2012/05/2012-MAY-Celebrate-Feast-by-Kazuya-Takahashi.jpg" align="left">

<br><br><br><br><br><br><br><br><br><br><br><br><br>
***
<b>Target Market:  </b>Customer base consists of males and those that are between the ages of 20-24.   
<ul style="list-style-type:square"><li><u>Recommendation</u>:Use Facebook Audience Insights and Google Analytics to learn more about this target audience.  Develop and implement a marketing campaign based on those insights.
</ul>
<b>The most profitable items are the most expensive:</b>  Aside from item 52, which lists as number 1 in "Top Sellers" and "Most Profitable", the higher priced items are generating the most revenue for the company.
<ul style="list-style-type:square"><li><u>Recommendation</u>:  Gather additional information through in-game data such such as item utilization and chat text, as well as surveying customers who made these purchases, to identify attributes/features that drove them to make these purchases.  Ensure we are incorporating these attributes/features into our product design strategy.</ul>

About 25% of total purchases were made by repeat customers.
<ul style="list-style-type:square"><li><u>Recommendation</u>:Conduct an analysis on those repeat customers.  Identify what drove them to make those repeat purchases through surveys and segmentation(gender/age). 
</ul>
</ul>



```python
#import 
import pandas as pd
import numpy as np
rawpurchasedata = "purchase_data.json"
sales_data = pd.read_json(rawpurchasedata)


```

<c><h3>Player Count</h3></c>



```python
#Create Dataframe with a unique count of players using SN as the unique identifier
pc_df = pd.DataFrame(
    {"Players Count": [sales_data["SN"].nunique()]
    })

pc_df



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Players Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>74</td>
    </tr>
  </tbody>
</table>
</div>



<c><h3>Purchasing Analysis (Total)</h3></c>


```python
#create lists with relevant fields

uniqueitems = sales_data["Item Name"].nunique()
average_price = [np.round(sales_data["Price"].mean(), 2)]
number_of_purchases = [sales_data["Price"].count()]
total_revenue =  [sales_data["Price"].sum()]
number_of_people= sales_data["SN"].nunique()

#create Dataframe with those lists
pa_df = pd.DataFrame(
    {"Number of Unique Items": uniqueitems ,"Average Price": average_price , 
     "Number of Purchases": number_of_purchases,"Total Revenue": total_revenue
    
    })
#change formating
pa_df["Average Price"] = pa_df["Average Price"].map("${:.2f}".format)
pa_df["Total Revenue"] = pa_df["Total Revenue"].map("${:.2f}".format)

#change column order
pa_df[['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']]


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63</td>
      <td>$2.92</td>
      <td>78</td>
      <td>$228.10</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Gender Demographics</h3>


```python
#find total number of unique players and assign to "total"
total=sales_data['SN'].nunique()
#groupby gender based on unique counts of those corresponding genders(based on SN); assign to ga1_uniquecount
ga1_uniquecount = sales_data.groupby(["Gender"])["SN"].nunique()

#create percent
ga1_percent= (ga1_uniquecount/total)*100
ga1_percent= ga1_percent.map("{:.2f}%".format)

#create new data frame based on unique count and percent
ga1 = pd.DataFrame(
    {"Percentage of Players": ga1_percent,
     "Total Count": ga1_uniquecount})

ga1 



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>17.04%</td>
      <td>99</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>81.76%</td>
      <td>475</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.20%</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Purchasing Analysis (Gender)</h3>


```python
#create multiple groupby objects 
countoft = sales_data
ga2_uniquecount = sales_data.groupby(["Gender"])["SN"].nunique()
ga2_purchase_count = sales_data.groupby(["Gender"])["SN"].count()
ga2_avg_puchase_price = sales_data.groupby(["Gender"])["Price"].mean()
ga2_ttl_purchase_price = sales_data.groupby(["Gender"])["Price"].sum()
ga2_nmlzd_totals = ga2_ttl_purchase_price/ga2_uniquecount
#change formatting
ga2_avg_puchase_price = ga2_avg_puchase_price.map("${:,.2f}".format)
ga2_ttl_purchase_price = ga2_ttl_purchase_price.map("${:,.2f}".format)
ga2_nmlzd_totals= ga2_nmlzd_totals.map("${:,.2f}".format)
#create new dataframe with groupby ibjects
ga2 = pd.DataFrame({"Purchase Count": ga2_purchase_count,
                    "Average Purchase Price":ga2_avg_puchase_price,
                    "Total Purchase Value":ga2_ttl_purchase_price,
                    "Normalized Totals":ga2_nmlzd_totals})
ga2 = ga2.round(2)
#change order
ga2[['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals']]

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>130</td>
      <td>$3.04</td>
      <td>$395.80</td>
      <td>$4.00</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>642</td>
      <td>$3.03</td>
      <td>$1,945.51</td>
      <td>$4.10</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>8</td>
      <td>$2.98</td>
      <td>$23.86</td>
      <td>$3.41</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Age Demographics</h3>


```python
#create unique total count based on SN; assign to total2
total2=sales_data['SN'].nunique()

#create dataframe
age_demo=pd.DataFrame(
    {"Age": sales_data['Age'],"Percentage of Players": sales_data['Age'],
     "Players Count": sales_data['Age'],})

#create a function that replaces age within the age_demo column with the corresponding tier
def agerange_func(row):
    if row['Age'] < [10]:
        val = "<10"
    elif(row['Age'] >=[10]) & (row['Age'] <=[14]):
        val = "10-14"
    elif(row['Age'] >=[15]) & (row['Age'] <=[19]):
        val = "15-19"   
    elif(row['Age'] >=[20]) & (row['Age'] <=[24]):
        val = "20-24"  
    elif(row['Age'] >=[25]) & (row['Age'] <=[29]):
        val = "25-29"  
    elif(row['Age'] >=[30]) & (row['Age'] <=[34]):
        val = "30-34"  
    elif(row['Age'] >=[35]) & (row['Age'] <=[39]):
        val = "35-39"  
    else:
        val = "40+"  
    return val
age_demo['Age'] = age_demo.apply(agerange_func, axis=1)

#create new dataframe
age_demoaba=pd.DataFrame(
    {"Age": age_demo['Age'],"SN":sales_data['SN']})

#calculate totals and change format
age_demoaba1 = age_demoaba.groupby(["Age"])["SN"].nunique()
age_demoaba2 = (age_demoaba.groupby(["Age"])["SN"].nunique()/total2*100)
age_demoaba2 = age_demoaba2.map("{:.2f}%".format)
age_demo2_f=pd.DataFrame(
    {"Percentage of Players": age_demoaba2,"Total Count": age_demoaba1})
del age_demo2_f.index.name

age_demo2_f
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>4.05%</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>14.86%</td>
      <td>11</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.95%</td>
      <td>34</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>10.81%</td>
      <td>8</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.11%</td>
      <td>6</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>8.11%</td>
      <td>6</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.35%</td>
      <td>1</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>6.76%</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Purchasing Analysis (Age)</h3>


```python
#create dataframe
age_demo2 = pd.DataFrame(
    {"Age": sales_data['Age'],"Purchase Count": sales_data['Age'],
    "Average Purchase Price": sales_data['Price'],
    "Total Purchase Value": sales_data['Price'],
    "Normalized Totals": sales_data['Price']})


#create a function that replaces age within the age_demo2 column with the corresponding tier
def agerange_func(row):
    if row['Age'] < [10]:
        val = "<10"
    elif(row['Age'] >=[10]) & (row['Age'] <=[14]):
        val = "10-14"
    elif(row['Age'] >=[15]) & (row['Age'] <=[19]):
        val = "15-19"   
    elif(row['Age'] >=[20]) & (row['Age'] <=[24]):
        val = "20-24"  
    elif(row['Age'] >=[25]) & (row['Age'] <=[29]):
        val = "25-29"  
    elif(row['Age'] >=[30]) & (row['Age'] <=[34]):
        val = "30-34"  
    elif(row['Age'] >=[35]) & (row['Age'] <=[39]):
        val = "35-39"  
    else:
        val = "40+"  
    return val
age_demo2['Age'] = age_demo2.apply(agerange_func, axis=1)

age_demo2a=pd.DataFrame(
    {"Age": age_demo2['Age'],"Average Purchase Price": age_demo2['Average Purchase Price']})


#calculate totals and change format
ad2_pc = age_demo2a.groupby(["Age"])["Average Purchase Price"].count()
ad2_avpp = age_demo2a.groupby(["Age"])["Average Purchase Price"].mean()
ad2_ttl = age_demo2a.groupby(["Age"])["Average Purchase Price"].sum()
ad2_nmzdttl11 =age_demo2a.groupby(["Age"])["Average Purchase Price"].nunique()
ad2_nmzdttl = ad2_ttl /ad2_nmzdttl11 

ad2_avpp= ad2_avpp.map("${:,.2f}".format)
ad2_ttl = ad2_ttl.map("${:,.2f}".format)
ad2_nmzdttl= ad2_nmzdttl.map("${:,.2f}".format)

age_demo3_f=pd.DataFrame(
    {"Purchase Count": ad2_pc,
    "Average Purchase Price": ad2_avpp,
    "Total Purchase Value": ad2_ttl,
    "Normalized Totals": ad2_nmzdttl})
del age_demo3_f.index.name

#reorder
age_demo3_f[['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>$2.98</td>
      <td>$92.42</td>
      <td>$3.19</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>132</td>
      <td>$3.08</td>
      <td>$406.62</td>
      <td>$4.73</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>316</td>
      <td>$3.01</td>
      <td>$950.59</td>
      <td>$7.67</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>137</td>
      <td>$3.05</td>
      <td>$417.21</td>
      <td>$5.03</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>62</td>
      <td>$2.93</td>
      <td>$181.40</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>54</td>
      <td>$3.18</td>
      <td>$171.50</td>
      <td>$4.08</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>11</td>
      <td>$3.41</td>
      <td>$37.47</td>
      <td>$3.75</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>37</td>
      <td>$2.92</td>
      <td>$107.96</td>
      <td>$3.37</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Top Spenders</h3>


```python
#create groupby objects and with relevant calculations
ts_c_df=pd.DataFrame(sales_data.groupby("SN")["Price"].count())
ts_avg_df=pd.DataFrame(sales_data.groupby("SN")["Price"].mean())
ts_ttl_df=pd.DataFrame(sales_data.groupby("SN")["Price"].sum())

#create dataframe with groupby objects
ts=pd.DataFrame(
    {"Purchase Count": ts_c_df['Price'], 
     "Average Purchase Price": (ts_avg_df['Price']).map("${:,.2f}".format),
     "Total Purchase Value": (ts_ttl_df['Price'])})

#sort, format, and rename
ts=ts.sort_values(["Total Purchase Value"], ascending=False)
ts["Total Purchase Value"] = ts["Total Purchase Value"].map("${:,.2f}".format)
ts[['Purchase Count','Average Purchase Price','Total Purchase Value']].head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chamalo71</th>
      <td>4</td>
      <td>$3.36</td>
      <td>$13.45</td>
    </tr>
    <tr>
      <th>Strithenu87</th>
      <td>4</td>
      <td>$3.21</td>
      <td>$12.83</td>
    </tr>
    <tr>
      <th>Mindosia50</th>
      <td>3</td>
      <td>$4.00</td>
      <td>$12.01</td>
    </tr>
    <tr>
      <th>Aeralria27</th>
      <td>3</td>
      <td>$3.79</td>
      <td>$11.38</td>
    </tr>
    <tr>
      <th>Eudai71</th>
      <td>3</td>
      <td>$3.79</td>
      <td>$11.37</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Most Popular Items</h3>


```python
#create groupby objects and with relevant calculations
mp1_c_df=pd.DataFrame(sales_data.groupby(['Item ID','Item Name']) ["Price"].count())
mp1_avg_df=pd.DataFrame(sales_data.groupby(["Item ID", "Item Name"])["Price"].mean())
mp1_ttl_df=pd.DataFrame(sales_data.groupby(["Item ID", "Item Name"])["Price"].sum())

#create dataframe with groupby objects
mp1=pd.DataFrame(
    {"Purchase Count": mp1_c_df['Price'], 
     "Item Price": (mp1_avg_df['Price']).map("${:,.2f}".format),
     "Total Purchase Value": (mp1_ttl_df['Price']).map("${:,.2f}".format)})

#sort, format, and rename
mp1=mp1.sort_values(["Purchase Count"], ascending=False)
mp1[['Purchase Count','Item Price','Total Purchase Value']].head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>52</th>
      <th>Hatred</th>
      <td>11</td>
      <td>$4.59</td>
      <td>$50.49</td>
    </tr>
    <tr>
      <th>174</th>
      <th>Primitive Blade</th>
      <td>9</td>
      <td>$1.39</td>
      <td>$12.51</td>
    </tr>
    <tr>
      <th>111</th>
      <th>Misery's End</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>91</th>
      <th>Celeste</th>
      <td>8</td>
      <td>$2.07</td>
      <td>$16.56</td>
    </tr>
    <tr>
      <th>143</th>
      <th>Frenzied Scimitar</th>
      <td>8</td>
      <td>$3.35</td>
      <td>$26.80</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Most Profitable Items</h3>


```python
#create groupby objects and with relevant calculations
mp2_c_df=pd.DataFrame(sales_data.groupby(['Item ID','Item Name']) ["Price"].count())
mp2_avg_df=pd.DataFrame(sales_data.groupby(["Item ID", "Item Name"])["Price"].mean())
mp2_ttl_df=pd.DataFrame(sales_data.groupby(["Item ID", "Item Name"])["Price"].sum())

#create dataframe with groupby objects
mp2=pd.DataFrame(
    {"Purchase Count": mp2_c_df['Price'], 
     "Item Price": (mp2_avg_df['Price']).map("${:,.2f}".format),
     "Total Purchase Value": (mp2_ttl_df['Price'])})

#sort, format, and rename
mp2=mp2.sort_values(["Total Purchase Value"], ascending=False).head(30)
mp2["Total Purchase Value"] = mp2["Total Purchase Value"].map("${:,.2f}".format)
mp2[['Purchase Count','Item Price','Total Purchase Value']].head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>52</th>
      <th>Hatred</th>
      <td>11</td>
      <td>$4.59</td>
      <td>$50.49</td>
    </tr>
    <tr>
      <th>111</th>
      <th>Misery's End</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>120</th>
      <th>Agatha</th>
      <td>8</td>
      <td>$4.93</td>
      <td>$39.44</td>
    </tr>
    <tr>
      <th>93</th>
      <th>Apocalyptic Battlescythe</th>
      <td>8</td>
      <td>$4.85</td>
      <td>$38.80</td>
    </tr>
    <tr>
      <th>49</th>
      <th>The Oculus, Token of Lost Worlds</th>
      <td>8</td>
      <td>$4.61</td>
      <td>$36.88</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
