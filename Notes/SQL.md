# Structured Query Language

```sql
SELECT [expression] AS [name], [expression] AS [name], FROM [table] WHERE [condition] ORDER BY [order]; 
```

Joining tables: `FROM Table1, Table2`

```sql
SELECT * FROM dogs, parents WHERE name=child;
```

Implicit syntax: comma and put all conditions in the WHERE clause

Explicit syntax: Use `FROM __ JOIN __ ON` and put matching conditions after ON

## Aliases and Dot Expressions

Joining a Table with itself

```sql
SELECT a.child AS first, b.child AS second FROM parents AS a, parents AS b WHERE a.parent = b.parent and a.child < b.child;
```

```sql
CREATE TABLE grandparents AS SELECT a.parent AS grandog, b.child AS granpup
    FROM parents AS a, parents AS b WHERE b.parent = a.child;

SELECT grandog FROM grandparents, dog AS c, dog AS d
    WHERE grandog = c.name AND
          granpup = d.name AND
          c.fur = d.fur;

```

## Numerical Expressions

## String Expressions

## Aggregate functions

max, min, avg, sum, count

arithmetic

```sql
select count(*) from animals;

select count(distinct legs) from animals;
```

An aggregate function also selects a row in the table, which **may be** meaningful.

## Grouping

```sql
select [columns] from [table] group by [expression] having [expression];
```

`having` clause filters the set of groups that are aggregated
