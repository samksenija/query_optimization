CREATE TABLE IF NOT EXISTS STATISTICS (
	id INT,
    executed_query TEXT,
    explain_query TEXT,
    explain_json TEXT,
    explain_tree TEXT,
    explain_analyze TEXT,
    duration VARCHAR(15),
    layer_tag ENUM('original', '1st', '2nd') DEFAULT 'original',
    column_distinctiveness VARCHAR(350),
    number_of_rows_per_table VARCHAR(250),
    change_applied VARCHAR(250),
    note VARCHAR(350),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM STATISTICS;
