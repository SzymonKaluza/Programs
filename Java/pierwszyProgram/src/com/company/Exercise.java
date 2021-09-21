package com.company;

import java.util.Scanner;

public class Exercise {
    public static void main(String[] args) {
        System.out.println("Podaj liczbę pierwszą: ");
        Scanner input = new Scanner(System.in);
        int firstNumber = input.nextInt();
        System.out.println("Podaj liczbę pierwszą: ");
        Scanner in = new Scanner(System.in);
        int secondNumber = in.nextInt();
        System.out.println("Suma podanych liczb wynosi: " + (firstNumber + secondNumber));
    }
}
