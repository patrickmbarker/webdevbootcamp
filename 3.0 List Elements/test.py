import shautils
import django

file = r"\\txaus.ds.sjhs.com\GroupDir\Analytics-Health-Economics\Analytics\Innovations_in_Healthcare_Delivery\Seton_Health_Alliance\ACO\SHARED_Folder_ACO_and_Analytics\From_Aetna_Archive\SETON_SI_AETNLABD_202401_20240219.txt"
print(shautils.check_file_exists(file))