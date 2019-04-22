from pathlib import Path
from csv import DictReader

# バッチファイル製造クラス
class BatchFileFactory(object):
    ## コンストラクタ

    def __init__(self, file_name):
        self.file_name = file_name

    ## プロパティ

    ### ファイル名
    @property
    def file_name(self):
        return self.__name

    @file_name.setter
    def file_name(self, file_name):
        self.__name = file_name
        self.__data_file = Path(self.__name)
        self.__directory = self.__data_file.parent

    ## メソッド

    ### バッチファイル生成
    def create(self):
        dest_dir = self.__directory.joinpath(self.__data_file.stem)
        dest_dir.mkdir(parents=True, exist_ok=True)

        with self.__data_file.open('r', encoding='utf_8_sig') as f:
            rows = DictReader(f, delimiter = ',', doublequote = True, lineterminator = '\r\n', quotechar = '"', skipinitialspace = True)
            for row in rows:
                file = row['file']
                jobname = row['jobname']
                bat = dest_dir.joinpath(jobname + '.bat')
                self.__write(bat, file)

    ### バッチファイル出力
    def __write(self, wf, call_file):
        with wf.open('w') as ws:
            body = f'cscript "..\{call_file}"\r\necho %ERRORLEVEL%'
            ws.write(body)
