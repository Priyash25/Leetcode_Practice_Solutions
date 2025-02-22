## https://platform.stratascratch.com/coding/514-marketing-campaign-success-advanced

Question ASK :Users with only one or multiple purchases on the first day do not count, nor do users who later buy only the same products from their first day.

- Since they say users with either one purchase or multiple purchase bu only on 1st day so we take them with 1st CTE of 1 time users
- Although redundant but we take bought only 1 product id ever
- Lastly we see members and join with 1st purchase to see if they ever bought a different product. If yes then they are affected by campaign


WITH one_time_users AS (
    SELECT user_id
    FROM marketing_campaign
    GROUP BY user_id
    HAVING COUNT(DISTINCT created_at) = 1
), 

same_product AS (
    SELECT user_id
    FROM marketing_campaign
    GROUP BY user_id
    HAVING COUNT(DISTINCT product_id) = 1
),

users_first_purchase AS (
    SELECT 
        user_id, 
        product_id, 
        created_at, 
        DENSE_RANK() OVER (PARTITION BY user_id ORDER BY created_at) AS rn
    FROM marketing_campaign
),

users_first_joined AS (
    SELECT 
        m1.user_id, 
        m1.product_id AS m1_product_id, 
        m2.product_id AS m2_product_id
    FROM marketing_campaign m1
    LEFT JOIN (
        SELECT user_id, product_id, created_at 
        FROM users_first_purchase 
        WHERE rn = 1
    ) m2
    ON m1.user_id = m2.user_id 
    AND m1.product_id = m2.product_id
)

SELECT COUNT(DISTINCT mc.user_id) AS user_count
FROM marketing_campaign mc
WHERE NOT EXISTS (SELECT 1 FROM one_time_users ou WHERE ou.user_id = mc.user_id)
AND NOT EXISTS (SELECT 1 FROM same_product sp WHERE sp.user_id = mc.user_id)
AND mc.user_id IN (SELECT user_id FROM users_first_joined WHERE m2_product_id IS NULL);
