"""Test using .NET (Unity API) from Python"""

import clr

clr.AddReference("DLL/DBIMX.FileConversionUtility.Common")
clr.AddReference("DLL/DBIMX.FileIdentification")

from System import *

from DBIMX.FileConversionUtility.Common.HelperClasses.Serializers import SettingsFileSerializer
from DBIMX.FileConversionUtility.Common.Models.Configuration import OperationSettings
from DBIMX.FileConversionUtility.Common.Models.Objects import FileDefinition
from DBIMX.FileConversionUtility.Common.Models.Enumerations import Operation, FileFormat
from System.Collections.Generic import List

def main() -> None:
    """Main process"""
    op_settings = OperationSettings()
    op_settings.Action = Operation.Convert
    op_settings.DestinationType = FileFormat.Pdf
    op_settings.SourceFiles = List[FileDefinition]()
    for file in [r"C:\Users\SMCLEAN\Desktop\Recent Cleanup\COMM MASS classify task.docx",
                 r"C:\Users\SMCLEAN\Desktop\Recent Cleanup\Extropy.html"]:
        op_settings.SourceFiles.Add(FileDefinition(file))

    # This results in ['OperationSettings' object has no attribute 'ToConfigFile']
    #      because pythonnet cannot execute extension methods
    # xml = op_settings.ToConfigFile(FileDefinition("test.fcu"))

    xml = SettingsFileSerializer.ToConfigFile(op_settings,
          FileDefinition(r"C:\Users\SMCLEAN\Desktop\test.fcu"))

    print(xml)

if __name__ == '__main__':
    main()
