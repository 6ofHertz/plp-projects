SELECT paymentDate, SUM(amount) AS totalAmount
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;
