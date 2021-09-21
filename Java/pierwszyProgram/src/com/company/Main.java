package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world");
        Scanner input = new Scanner(System.in);
        System.out.println("Podaj liczbę: ");
        int number = input.nextInt();
        System.out.println("Twoja liczba to: "+ number);

    }
}
