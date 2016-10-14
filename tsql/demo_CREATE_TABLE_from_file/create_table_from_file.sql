IF OBJECT_ID('Test.dbo.markers','U') IS NOT NULL
	DROP TABLE [Test].[dbo].[markers];

CREATE TABLE [Test].[dbo].[markers]
    (
    [rsID] varchar(500)
    )

    BULK INSERT [Test].[dbo].[markers] FROM 'E:\rqtl_pipeline\test\markers.txt'
    WITH (FORMATFILE = 'E:\cgottsacker\mssms\FILEFORMAT.XML')