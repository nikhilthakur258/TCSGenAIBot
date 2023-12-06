import org.openqa.selenium.By;  
import org.openqa.selenium.WebDriver;  
import org.openqa.selenium.WebElement;  
import org.openqa.selenium.chrome.ChromeDriver;  
  
public class ExampleTest {  
    public static void main(String[] args) throws InterruptedException {  
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");  
        WebDriver driver = new ChromeDriver();  
        driver.get("https://www.example.com");  
  
        // Click on "Upload Files"  
        WebElement uploadButton = driver.findElement(By.linkText("Upload Files"));  
        uploadButton.click();  
  
        // Wait for the page to reload  
        Thread.sleep(1000);  
  
        // Click on "Spreadsheet Formats"  
        WebElement spreadsheetButton = driver.findElement(By.linkText("Spreadsheet Formats"));  
        spreadsheetButton.click();  
  
        // Verify that "XLS" and "XLSX" buttons show  
        WebElement xlsButton = driver.findElement(By.xpath("//button[text()='XLS']"));  
        WebElement xlsxButton = driver.findElement(By.xpath("//button[text()='XLSX']"));  
        assert xlsButton.isDisplayed();  
        assert xlsxButton.isDisplayed();  
  
        // Click on "XLSX" and select "500kb-sheet.xlsx"  
        xlsxButton.click();  
        WebElement fileInput = driver.findElement(By.name("file"));  
        fileInput.sendKeys("/path/to/500kb-sheet.xlsx");  
  
        // Wait for the upload to complete  
        Thread.sleep(5000);  
  
        // Verify that "500kb-sheet.xlsx" is in the "Uploaded Files" table  
        WebElement uploadedTable = driver.findElement(By.id("uploaded-files"));  
        WebElement cell = uploadedTable.findElement(By.xpath("//td[text()='500kb-sheet.xlsx']"));  
        assert cell.isDisplayed();  
  
        // Click on "XLSX" and select "1mb-sheet.xlsx"  
        xlsxButton.click();  
        fileInput.sendKeys("/path/to/1mb-sheet.xlsx");  
  
        // Wait for the upload to fail  
        Thread.sleep(5000);  
  
        // Verify that "1mb-sheet.xlsx" is not in the "Uploaded Files" table  
        try {  
            WebElement cell2 = uploadedTable.findElement(By.xpath("//td[text()='1mb-sheet.xlsx']"));  
            assert !cell2.isDisplayed();  
        } catch (Exception e) {}  
  
        // Click on "Login" and sign in with testuser123/$Pass123  
        WebElement loginButton = driver.findElement(By.linkText("Login"));  
        loginButton.click();  
        WebElement usernameInput = driver.findElement(By.name("username"));  
        WebElement passwordInput = driver.findElement(By.name("password"));  
        WebElement signinButton = driver.findElement(By.xpath("//button[text()='Sign in']"));  
        usernameInput.sendKeys("testuser123");  
        passwordInput.sendKeys("$Pass123");  
        signinButton.click();  
  
        // Wait for the page to reload  
        Thread.sleep(1000);  
  
        // Verify that "500kb-sheet.xlsx" is still in the "Uploaded Files" table  
        cell = uploadedTable.findElement(By.xpath("//td[text()='500kb-sheet.xlsx']"));  
        assert cell.isDisplayed();  
  
        // Verify that "1mb-sheet.xlsx" is not in the "Uploaded Files" table  
        try {  
            WebElement cell2 = uploadedTable.findElement(By.xpath("//td[text()='1mb-sheet.xlsx']"));  
            assert !cell2.isDisplayed();  
        } catch (Exception e) {}  
  
        // Click on "Spreadsheet Formats" again  
        spreadsheetButton.click();  
  
        // Verify that "XLS" and "XLSX" buttons show  
        assert xlsButton.isDisplayed();  
        assert xlsxButton.isDisplayed();  
  
        // Click on "XLSX" and select "1mb-sheet.xlsx" again  
        xlsxButton.click();  
        fileInput.sendKeys("/path/to/1mb-sheet.xlsx");  
  
        // Wait for the upload to complete  
        Thread.sleep(5000);  
  
        // Verify that "1mb-sheet.xlsx" is in the "Uploaded Files" table  
        WebElement cell2 = uploadedTable.findElement(By.xpath("//td[text()='1mb-sheet.xlsx']"));  
        assert cell2.isDisplayed();  
  
        // Verify that "500kb-sheet.xlsx" is still in the "Uploaded Files" table  
        cell = uploadedTable.findElement(By.xpath("//td[text()='500kb-sheet.xlsx']"));  
        assert cell.isDisplayed();  
  
        driver.quit();  
    }  
}  
