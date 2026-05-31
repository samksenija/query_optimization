CREATE TABLE IF NOT EXISTS STATISTICS (
	id INT,
    executed_query TEXT,
    execution_plan TEXT,
    cost TEXT,
    layer_tag ENUM('original', '1st', '2nd') DEFAULT 'original',
    change_applied TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM STATISTICS;
