CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE receipts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    shop_name VARCHAR(50),
    date DATE,
    total NUMERIC(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE receipt_items (
    receipt_id INTEGER NOT NULL,
    item_name VARCHAR(50),
    price NUMERIC(10,2),
    PRIMARY KEY (receipt_id, item_name),
    FOREIGN KEY (receipt_id) REFERENCES receipts(id) ON DELETE CASCADE
);

-- OPTIONAL
CREATE TABLE user_receipts (
    user_id INTEGER NOT NULL,
    receipt_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, receipt_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receipt_id) REFERENCES receipts(id) ON DELETE CASCADE
);

