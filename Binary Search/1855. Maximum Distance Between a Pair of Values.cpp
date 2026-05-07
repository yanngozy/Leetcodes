class Solution {
public:
    int bissect(vector<int>& arr, int x, int debut) {
        int i = debut, j = arr.size() - 1;
        while (i < j - 1) {
            int mid = i + (j - i) / 2;
            if (arr[mid] >= x) {
                i = mid;
            } else {
                j = mid - 1;
            }
        }
        if (arr[j] >= x) return j - debut;
        return i - debut;
    }

    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int m = min((int)nums1.size() - 1, (int)nums2.size() - 1);
        int res = 0;
        for (int i = 0; i <= m; i++) {
            if (nums2[i] >= nums1[i]) {
                res = max(res, bissect(nums2, nums1[i], i));
            }
        }
        return res;
    }
};

Time complexity: O(nlog(n)) 
space complexity: O(1)
