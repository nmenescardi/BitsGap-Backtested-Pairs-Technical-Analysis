
-- DROP DATABASE IF EXISTS bitsgap_ta;

CREATE DATABASE IF NOT EXISTS bitsgap_ta;
USE bitsgap_ta;


CREATE TABLE IF NOT EXISTS pairs (
	pair_id INT AUTO_INCREMENT PRIMARY KEY,
	symbol VARCHAR(20) NOT NULL,
	exchanger VARCHAR(30) NOT NULL DEFAULT "BINANCE",
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	UNIQUE KEY pair_symbol_exchanger (symbol, exchanger)
);


CREATE TABLE IF NOT EXISTS batches (
	batch_id INT AUTO_INCREMENT PRIMARY KEY,
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
);


CREATE TABLE IF NOT EXISTS batches_pairs (
	pair_id INT,
	batch_id INT,
	profit FLOAT(5) NOT NULL DEFAULT 0,
	category VARCHAR(10) NOT NULL DEFAULT '',
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (pair_id) REFERENCES pairs (pair_id),
	FOREIGN KEY (batch_id) REFERENCES batches (batch_id),
	UNIQUE KEY batches_pairs_single_row (pair_id, batch_id, category)
);


CREATE TABLE IF NOT EXISTS indicators (
	indicator_id INT AUTO_INCREMENT PRIMARY KEY,
	pair_id INT,
	batch_id INT,
	indicator_key VARCHAR(255) NOT NULL,
	indicator_value VARCHAR(255),
	timeframe VARCHAR(5),
	created_date DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
	last_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
	FOREIGN KEY (pair_id) REFERENCES pairs (pair_id),
	FOREIGN KEY (batch_id) REFERENCES batches (batch_id),
	UNIQUE KEY indicators_single_value (pair_id, batch_id, indicator_key, timeframe)
);

