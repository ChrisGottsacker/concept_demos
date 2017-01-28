/* Copied from ClearLogic's answer at http://stackoverflow.com/a/12504496/5149671
 * 
 * 
 */

IF OBJECT_ID('tempTable','U') IS NOT NULL
	DROP TABLE [tempTable];

CREATE TABLE [tempTable]
    (
    [rsID] varchar(500)
    )

    BULK INSERT [tempTable] FROM 'E:\path\to\file.txt'
    WITH (FORMATFILE = 'E:\path\to\FILE_FORMAT.xml')