USE geecoin;

-- Insert sample data into incomes table
INSERT INTO incomes (title, description, amount, date) VALUES
('Salary', 'Monthly salary', 3000.00, '2023-01-01'),
('Freelance Project', 'Payment for freelance project', 1500.00, '2023-01-15'),
('Investment', 'Return on investment', 500.00, '2023-01-20');

-- Insert sample data into expenses table
INSERT INTO expenses (title, description, amount, date) VALUES
('Rent', 'Monthly rent payment', 1000.00, '2023-01-05'),
('Groceries', 'Weekly groceries', 200.00, '2023-01-10'),
('Utilities', 'Monthly utilities payment', 150.00, '2023-01-12');