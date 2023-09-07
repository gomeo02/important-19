SELECT
  COUNT(DISTINCT tx_from) AS unique,
  COUNT(tx_from) AS total
FROM
  dex."trades"
WHERE
  tx_to = '\x881d40237659c251811cec9c364ef91dc08d300c'  -- MetaMash Swap Contract
end
