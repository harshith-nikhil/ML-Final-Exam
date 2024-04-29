library(arules)

transactions <- list(
  c("Laptop", "Laptop Bag", "USB-C Adapter"),
  c("Smartphone", "Screen Protector", "USB-C Adapter"),
  c("Laptop", "Laptop Bag"),
  c("Smartphone"),
  c("Book", "Bookmark"),
  c("Book", "Reading Light", "Bookmark"),
  c("Smartphone", "Phone Case", "Screen Protector"),
  c("USB-C Adapter"),
  c("Laptop", "Laptop Bag", "Smartphone"),
  c("Smartphone", "Phone Case")
)

trans <- as(transactions, "transactions")

inspect(trans)

frequent_itemsets <- apriori(trans, parameter = list(supp = 0.2, target = "frequent itemsets"))
inspect(frequent_itemsets)

rules <- apriori(trans, parameter = list(supp = 0.2, conf = 0.7, target = "rules"))
inspect(rules)

specific_antecedent_rules <- subset(rules, subset = items %in% "Phone Case")
inspect(specific_antecedent_rules)

consequents <- labels(rhs(specific_antecedent_rules))
print(consequents)
