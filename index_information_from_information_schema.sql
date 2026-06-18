SELECT 
    TABLE_NAME AS 'Table',
    INDEX_NAME AS 'Index Name',
    COLUMN_NAME AS 'Column',
    SEQ_IN_INDEX AS 'Sequence',
    NON_UNIQUE AS 'Can Have Duplicates (1=Yes, 0=No)',
    INDEX_TYPE AS 'Index Type'
FROM 
    INFORMATION_SCHEMA.STATISTICS
WHERE 
    TABLE_SCHEMA = 'tpch'
ORDER BY 
    TABLE_NAME, 
    INDEX_NAME, 
    SEQ_IN_INDEX;