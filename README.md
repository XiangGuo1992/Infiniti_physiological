# Infiniti_physiological
Physiological data (from Infiniti Raw output) analysis with python.

From the output .txt file with 5 channels' raw signal(Time, EKG(2048Hz), BVP(256Hz), Abd Resp(36Hz), Event(NM or start)) to the data needed such as Heart Rate and Breath Rate.

## Data structure
In the Raw .txt file, there are 5 channels' raw signal(Time, EKG(2048Hz), BVP(256Hz), Abd Resp(36Hz), Event(NM or start)) and some headers , describing the overall information of the experiment.

## 0_cleanInfinitiRawData.py
This script can delete the headers in the .txt file and output regulated data sheet.

![Image of Yaktocat](https://github.com/XiangGuo1992/Infiniti_physiological/blob/master/image/Cleaned.JPG)

## 0_time sycronization for Infiniti.py
This script can extract the preferred section from the the data, for example, 'start' Event in Column Event. This one also checked the time sycronization table 'time syncronization.csv', which is not needed in many other cases.

## 1_Calculat HR from raw Infiniti data.py
Calculate Heart Rate from the raw signal data, sampling_rate=2048.
biosppy library should be installed first.

## 1_Calculat BR from raw Infiniti data.py
Similar to the HR, this sript can calculate the respiratory rate, sampling_rate=32.

## 2.Converge subjects result.py
Converge data from the same subject into one table.

