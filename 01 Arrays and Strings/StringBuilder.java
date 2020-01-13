// ref to https://codereview.stackexchange.com/questions/133036/a-custom-string-builder-implementation

import java.util.ArrayList; 

public class StringBuilder{
    private ArrayList<String> array;
    private int size;

    public StringBuilder(){
        array = new ArrayList<>();
        size = 0;
    }

    public void add(String s){
        array.add(s);
        size += s.length();
    }

    public String toString(){
        char[] output = new char[size];
        int outputIndex = 0;

        for(int i = 0; i < array.size(); i++){
            for(int j = 0; j < array.get(i).length(); j++){
                output[outputIndex++] = array.get(i).charAt(j);
            }
        }

        return new String(output);

    }

    public static void main(String[] args) {
        StringBuilder s = new StringBuilder();
        s.add("Hello ");
        s.add("world!");
        System.out.println(s.toString());
    }
}