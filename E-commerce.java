import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Main {

    static class Order implements Comparable<Order> {
        int price;
        String shopID;
        String customerID;
        int timeInSeconds;

        public Order(String customerID, String shopID, int price, String timePoint) {
            this.customerID = customerID;
            this.shopID = shopID;
            this.price = price;
            this.timeInSeconds = timeToSeconds(timePoint);
        }
        
        @Override
        public int compareTo(Order other) {
            return Integer.compare(this.timeInSeconds, other.timeInSeconds);
        }
    }

    private static List<Order> orders = new ArrayList<>();
    private static List<String> queries = new ArrayList<>();
    private static Map<String, Integer> shopRevenueMap = new HashMap<>();
    private static Map<String, Map<String, Integer>> customerShopRevenueMap = new HashMap<>();
    private static int totalRevenue = 0;
    private static List<Integer> prefixSums = new ArrayList<>();
    private static StringBuilder output = new StringBuilder();

    public static void main(String[] args) throws IOException, ParseException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String currentBlock = "orders";
        String line;

        while ((line = reader.readLine()) != null) {
            line = line.trim();
            if (line.equals("#")) {
                currentBlock = currentBlock.equals("orders") ? "queries" : null;
                if (currentBlock == null) break;
                continue;
            }

            if (currentBlock.equals("orders")) {
                String[] parts = line.split(" ");
                String customerID = parts[0];
                String productID = parts[1];
                int price = Integer.parseInt(parts[2]);
                String shopID = parts[3];
                String timePoint = parts[4];

                Order order = new Order(customerID, shopID, price, timePoint);
                orders.add(order);

                totalRevenue += price;
                shopRevenueMap.put(shopID, shopRevenueMap.getOrDefault(shopID, 0) + price);

                customerShopRevenueMap.putIfAbsent(customerID, new HashMap<>());
                Map<String, Integer> shopMap = customerShopRevenueMap.get(customerID);
                shopMap.put(shopID, shopMap.getOrDefault(shopID, 0) + price);
            } else if (currentBlock.equals("queries")) {
                queries.add(line);
            }
        }

        orders.sort(Comparator.naturalOrder());
        computePrefixSums();
        processQueries(queries);
        System.out.print(output);
    }

    private static void computePrefixSums() {
        int currentSum = 0;
        for (Order order : orders) {
            currentSum += order.price;
            prefixSums.add(currentSum);
        }
    }

    private static int totalNumberOrders() {
        return orders.size();
    }

    private static int totalRevenue() {
        return totalRevenue;
    }

    private static int revenueOfShop(String shopID) {
        return shopRevenueMap.getOrDefault(shopID, 0);
    }

    private static int totalConsumeOfCustomerShop(String customerID, String shopID) {
        return customerShopRevenueMap.getOrDefault(customerID, new HashMap<>()).getOrDefault(shopID, 0);
    }

    private static int totalRevenueInPeriod(String fromTime, String toTime) {
        int fromTimeSec = timeToSeconds(fromTime);
        int toTimeSec = timeToSeconds(toTime);

        int startIdx = findStartIndex(fromTimeSec);
        int endIdx = findEndIndex(toTimeSec);

        if (startIdx == -1 || endIdx == -1 || startIdx > endIdx) return 0;
        return prefixSums.get(endIdx) - (startIdx > 0 ? prefixSums.get(startIdx - 1) : 0);
    }

    private static int findStartIndex(int fromTimeSec) {
        int low = 0, high = orders.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (orders.get(mid).timeInSeconds >= fromTimeSec) high = mid - 1;
            else low = mid + 1;
        }
        return low < orders.size() ? low : -1;
    }

    private static int findEndIndex(int toTimeSec) {
        int low = 0, high = orders.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (orders.get(mid).timeInSeconds <= toTimeSec) low = mid + 1;
            else high = mid - 1;
        }
        return high >= 0 ? high : -1;
    }

    private static void processQueries(List<String> queries) throws ParseException {
        for (String query : queries) {
            if (query.equals("?total_number_orders")) {
                output.append(totalNumberOrders()).append("\n");
            } else if (query.equals("?total_revenue")) {
                output.append(totalRevenue()).append("\n");
            } else if (query.startsWith("?revenue_of_shop")) {
                String[] parts = query.split(" ");
                output.append(revenueOfShop(parts[1])).append("\n");
            } else if (query.startsWith("?total_consume_of_customer_shop")) {
                String[] parts = query.split(" ");
                output.append(totalConsumeOfCustomerShop(parts[1], parts[2])).append("\n");
            } else if (query.startsWith("?total_revenue_in_period")) {
                String[] parts = query.split(" ");
                output.append(totalRevenueInPeriod(parts[1], parts[2])).append("\n");
            }
        }
    }

    private static int timeToSeconds(String time) {
        String[] parts = time.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        int seconds = Integer.parseInt(parts[2]);
        return hours * 3600 + minutes * 60 + seconds;
    }
}
