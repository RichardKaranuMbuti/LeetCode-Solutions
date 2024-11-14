#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

// Function to calculate the optimal cost and sum of differences
int calculate_optimal_cost(const vector<int>& arr, int x) {
    int n = arr.size();
    int total_sum_diff = 0;
    vector<int> prefix_sums(n + 1, 0);

    // Calculate prefix sums
    for (int i = 0; i < n; ++i) {
        prefix_sums[i + 1] = prefix_sums[i] + arr[i];
    }

    // Evaluate each starting position for the subarray
    for (int i = 0; i < n; ++i) {
        int left = i, right = n;
        
        // Binary search for the largest end position j where the optimal cost <= x
        while (left < right) {
            int mid = (left + right) / 2;
            int size = mid - i + 1;

            // Check pairing for matching cost
            int matching_cost = 0;
            for (int j = 0; j < size / 2; ++j) {
                matching_cost = max(matching_cost, arr[i + j] + arr[mid - j]);
            }

            if (size % 2 == 1) {
                matching_cost = max(matching_cost, arr[i + size / 2]);
            }

            if (matching_cost <= x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // Sum up the differences for all valid subarrays ending at `left`
        for (int j = i; j < left; ++j) {
            total_sum_diff += arr[j] - arr[i];
        }
    }

    return total_sum_diff;
}

// Process multiple queries
vector<int> process_queries(const vector<int>& arr, const vector<int>& queries) {
    vector<int> results;
    for (int x : queries) {
        results.push_back(calculate_optimal_cost(arr, x));
    }
    return results;
}

int main() {
    int n, q;
    cin >> n >> q;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    
    vector<int> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i];
    }
    
    // Output results for each query
    vector<int> results = process_queries(arr, queries);
    for (int result : results) {
        cout << result << endl;
    }
    
    return 0;
}
