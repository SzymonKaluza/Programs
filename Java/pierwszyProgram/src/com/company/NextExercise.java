package com.company;

import java.util.Scanner;

public class NextExercise {
    public static void main(String[] args) {
        System.out.println("podaj promień koła: ");
        Scanner secondScanner = new Scanner(System.in);
        int promien = secondScanner.nextInt();
        System.out.println("Obwód koła wynosi: " + (3.14 * promien * promien));

    }
}
