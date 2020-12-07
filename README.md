# 資科期末整理

## Dateset

[**來源**](https://www.kaggle.com/chrischien17/taiwan-taipei-city-real-estate-transaction-records?select=taipei_city_real_estate_transaction_v2.csv)

* district: 行政區域
    * 字串 
    * ('Daan District', 'shihlin', 'Nangang District', 'Songshan District', 'Neihu District', 'Beitou', 'Zhongzheng District', 'Wenshan District', 'Xinyi District', 'Datong District', 'Zhongshan Area', 'Wanhua District')
    * [1,0,0,0,0,0,0,0]
    * [0,1,0,0,0,0,0,0]
    * [0,0,1,0,0,0,0,0]
* transaction_type: 附屬物
    * 字串 
    * ('Land', 'Garage', 'Premises (land + building)', 'Building', 'Premises (land + building) + parking space')
    * [1,0,0]
    * [0,1,0]
    * [1,0,1]
    * ...
* land_shift_area: 土地坪數(平方公尺)
    * 浮點數
* urbanland_use: 用途，住宅or商用等等
    * 字串，六種可能
    * (others, work, quotient, address, other, Agriculture)
* mainuse: 更詳細的用途，但有些不明確。
    * 字串，考慮刪除(+2)
    * （'Residential business', 'For work', 'For business', 'See license', 'See other registration items', 'industrial use', 'Parking space', 'Resident', 'For commercial use'）
* main_building_material: 建材
    * 字串 
    * ('Wooden', 'Not Applicable', 'Earthwork', 'Stone building', 'Earthen masonry', 'See other registration items', 'Reinforced concrete construction', 'Civil engineering', 'Strengthen brickwork', 'Brickwork', 'Wall type reinforced concrete construction', 'Prestressed concrete construction', 'Steel reinforced concrete construction', 'See license')
* complete_year: 屋齡
    * 浮點數
* buildingshifttotal_area: 建物坪數
    * 浮點數
* num_room: 房間數
    * 整數
* num_hall: 大廳數
    * 整數
* num_toilet: 廁所數
    * 整數
* num_partition: 有無partition(無房間、無大廳、無廁所)
    * 布林，無很少
* management_org: 是否擁有管理組織
    * 布林
* total_ntd: 總價格
    * 整數
* **unit_ntd: 每平方公尺的價格**
    * 浮點數
    * **預測目標**
* carpark_category: 停車位種類
    * 字串
    * ('Tower parking', 'Lifting plane', 'Other', 'Lifting machinery', 'Ramp plane', 'Not Applicable', 'Ground floor', 'Ramp machinery')
* carpark_shift_area: 停車位大小(square meter)
    * 浮點數，一堆`0`，因為沒有停車位
* carpark_ntd: 停車位價錢
    * 整數，一堆`0`，因為沒有停車位
* transaction_year: 交易年份
    * 整數，絕大多數都是2019，考慮刪除欄位，並只留下2019後(含)的資料
* transaction_month: 交易月份
    * 整數
* building_age: 建物完成日期
    * 浮點數，考慮刪除，留下完成年份即可
* number_of_land: number of land in a transaction
    * 整數，不太懂意義，考慮刪除
* number_of_building: 建築物數量
    * 整數
* number_of_carpark: 停車位數目
    * 整數

## 處理注意事項

* 字串轉數字
    * 使用[one hot encoding](https://medium.com/@PatHuang/%E5%88%9D%E5%AD%B8python%E6%89%8B%E8%A8%98-3-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-label-encoding-one-hot-encoding-85c983d63f87)
* 刪除不必要欄位
* 房屋、土地分開處理，免得資料互相影響。可以之後分別預測。
    * 根據urbanland_use分資料
    * Others, other drop
