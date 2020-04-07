import pytest
import pandas as pd
from pandas._testing import assert_frame_equal
from datetime import datetime

from files_to_dataframe import FileToDF


# class TestFileToDF(unittest.TestCase):
class TestFileToDF():
    # an instance
    testing_txt_to_df = FileToDF('data8-engineering-project', 'Test_txt')
    testing_csv_to_df = FileToDF('data8-engineering-project', 'Test_csv')

    def test_bucket(self):
        assert self.testing_txt_to_df.bucket == 'data8-engineering-project'

    def test_item_in_folder_txt(self):
        assert self.testing_txt_to_df.folder == 'Test_txt'

    def test_item_in_folder_csv(self):
        assert self.testing_csv_to_df.folder == 'Test_csv'

    def test_file_name_dict_txt(self):
        assert self.testing_txt_to_df.file_names_dict == {'Test_txt': ['txt_file1_test.txt', 'txt_file2_test.txt']}

    def test_file_name_dict_csv(self):
        assert self.testing_csv_to_df.file_names_dict == {'Test_csv': ['csv_file1_academy_test.csv',
                                                                       'csv_file2_academy_test.csv']}

    def test_filenames_txt(self):
        assert self.testing_txt_to_df.filenames()[0][0]['Key'] == 'Test_txt/txt_file1_test.txt'

    def test_filenames_csv(self):
        # the function filenames returns: [[{'Key': 'Test_csv/csv_file1_academy_test.csv', 'LastModified':
        # datetime.datetime(2020, 4, 6, 22, 4, 53, tzinfo=tzutc()), 'ETag': '"fa212b370804932337f6e47e0c749be0"', '
        # Size': 143, 'StorageClass': 'STANDARD'}], [{'Key': 'Test_csv/csv_file2_academy_test.csv', 'LastModified':
        # datetime.datetime(2020, 4, 6, 22, 4, 53, tzinfo=tzutc()), 'ETag': '"43e6f50fab21c626cc089a3626907e08"',
        # 'Size': 119, 'StorageClass': 'STANDARD'}]]
        assert self.testing_csv_to_df.filenames()[0][0]['Key'] == 'Test_csv/csv_file1_academy_test.csv'


    def test_dataframe_txt(self):
        df_test = self.testing_txt_to_df.dataframetxt()
        date1 = datetime.strptime('2019-12-05', '%Y-%m-%d')
        date2 = datetime.strptime('2019-10-01', '%Y-%m-%d')
        df_result = pd.DataFrame({'name': ['Tobe Markovic ', 'Konstantine Giacomoni '],
                                  'psychometrics':[62, 40],
                                  'psycho.max': [100, 100],
                                  'presentation':[20, 21],
                                  'present.max': [32, 32],
                                  'academy': ['Birmingham', 'London'],
                                  'date': [date1, date2]}, index=[0,0])
        assert df_test.equals(df_result) #assert_frame_equal(df_test, df_result)

    def test_dataframe_csv(self):
        df_test = self.testing_csv_to_df.dataframecsv()
        df_result = pd.DataFrame({"name": ["Loree Abbot", "Tedmund Emanulsson", "Bobine Brodie", "Guilbert Leet",
                                           "Bren Tomei", "Ron Fincke"],
                                  "trainer": ["Elly Kelly", "Elly Kelly", "Elly Kelly", "Shaunie Hovis",
                                              "Shaunie Hovis", "Shaunie Hovis"],
                                  "IH_W1": [5, 4, 1, 4, 3, 4],
                                  "IS_W1": [4, 2, 3, 6, 5, 7],
                                  "PV_W1": [5, 3, 5, 7, 6, 7],
                                  "PS_W1": [4, 6, 1, 9, 8, 8]}, index=[0,1,2,0,1,2])
        assert df_test.equals(df_result)  #assert_frame_equal(df_test, df_result)

