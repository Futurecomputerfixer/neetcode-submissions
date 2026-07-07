class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s: strs)
            sb.append(s.length()).append("#").append(s);
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();
        int i = 0;
        int len = str.length();
        while(i < len){
            int j = i;
            while(str.charAt(j) != '#')j++;
            int length = Integer.valueOf(str.substring(i, j));
            i = j + length + 1;
            list.add(str.substring(j + 1, i));
        }
        return list;
    }
}
