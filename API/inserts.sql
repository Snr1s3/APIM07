USE geecoin;

-- Insert sample data into incomes table
INSERT INTO incomes (title, description, amount, date) VALUES
('Salary', 'Monthly salary', 3000.00, '2023-01-01'),
('Freelance Project', 'Payment for freelance project', 1500.00, '2023-01-15'),
('Investment', 'Return on investment', 500.00, '2023-01-20'),
('Bonus', 'Year-end bonus', 2000.00, '2023-01-25'),
('Gift', 'Birthday gift', 300.00, '2023-02-01'),
('Sale', 'Sale of old laptop', 400.00, '2023-02-10'),
('Dividends', 'Stock dividends', 250.00, '2023-02-15'),
('Refund', 'Tax refund', 1200.00, '2023-02-20'),
('Lottery', 'Lottery winnings', 100.00, '2023-02-25'),
('Interest', 'Bank interest', 50.00, '2023-03-01');

-- Insert sample data into expenses table
INSERT INTO expenses (title, description, amount, date) VALUES
('Rent', 'Monthly rent payment', 1000.00, '2023-01-05'),
('Groceries', 'Weekly groceries', 200.00, '2023-01-10'),
('Utilities', 'Monthly utilities payment', 150.00, '2023-01-12'),
('Transport', 'Monthly transport pass', 100.00, '2023-01-15'),
('Insurance', 'Health insurance', 300.00, '2023-01-20'),
('Dining', 'Dinner at restaurant', 80.00, '2023-01-25'),
('Entertainment', 'Movie tickets', 50.00, '2023-02-01'),
('Clothing', 'New clothes', 200.00, '2023-02-10'),
('Subscription', 'Monthly subscription', 30.00, '2023-02-15'),
('Maintenance', 'Car maintenance', 250.00, '2023-02-20');