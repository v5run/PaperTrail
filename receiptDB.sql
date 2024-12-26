CREATE TABLE users (
    user_id SERIAL,
    username varchar(50),
    email varchar(50),
    PRIMARY KEY(user_id)
    );

CREATE TABLE receipts (
    user_id varchar(255),
    id SERIAL,
    shop_name varchar(50),
    date DATE,
    total NUMERIC(10,2),
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE receipt_items (
    id SERIAL REFERENCES receipts(id),
    item_name varchar(50),
    price NUMERIC(10,2),
    PRIMARY KEY (id, item_name)
);

