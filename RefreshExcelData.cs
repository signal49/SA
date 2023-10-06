

using Microsoft.Office.Interop.Excel;
public partial class Program
{
    public static void Main()
    {
        //Console.WriteLine("Hello, world");
        // Create an instance of Excel application
        Microsoft.Office.Interop.Excel.Application excelApp = new Microsoft.Office.Interop.Excel.Application();

        // Set the visibility of the Excel application to false
        excelApp.Visible = false;
        var workbookPath = "C:\\Users\\lenovo\\Desktop\\fintech\\Pivot.xlsx";
        // Open the workbook
        Workbook excelWorkbook = excelApp.Workbooks.Open(workbookPath);

        // Refresh all data in the workbook
        excelWorkbook.RefreshAll();

        // Save the workbook
        excelWorkbook.Save();

        // Close the workbook and release resources
        excelWorkbook.Close(false, workbookPath, null);
        System.Runtime.InteropServices.Marshal.ReleaseComObject(excelWorkbook);
        excelWorkbook = null;

        // Quit Excel application and release resources
        excelApp.Quit();
        System.Runtime.InteropServices.Marshal.ReleaseComObject(excelApp);
        excelApp = null;

    }

}
//Console.WriteLine("Hello, World!");
