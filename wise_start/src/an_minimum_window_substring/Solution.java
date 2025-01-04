package an_minimum_window_substring;

import java.util.HashMap;

public class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> t_map = new HashMap<>();
        for (char ch: t.toCharArray()) {
            int val = t_map.getOrDefault(ch, 0) + 1;
            t_map.put(ch, val);
        }


        HashMap<Character, Integer> window_map = new HashMap<>();
        int left = 0;
        for (int idx = 0; idx < s.length(); idx++) {
            char ch = s.charAt(idx);
            if (t_map.containsKey(ch)) {
                int val = window_map.getOrDefault(ch, 0) + 1;
                window_map.put(ch, val);
            }

            // if `window_map` contains AT LEAST all the kv pairs in `t_map`
            // do sumn
        }
        return "";
    }
}
