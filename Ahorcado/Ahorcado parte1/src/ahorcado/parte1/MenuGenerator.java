/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ahorcado.parte1;

import java.util.Scanner;

/**
 *
 * @author Araceli,Diego,Óscar
 */
public class MenuGenerator {

    HangMan hangMan;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        MenuGenerator menuGenerator = new MenuGenerator();
        menuGenerator.hangMan = new HangMan(menuGenerator.showInitMenu());
        menuGenerator.showGameMenu();

    }

    private String showInitMenu() {
        WordGenerator palabraSecr = new WordGenerator();
        return palabraSecr.generateWord();
    }

    private void showGameMenu() {
        Scanner scan = new Scanner(System.in);
        System.out.println(hangMan.getStringFails());
        System.out.println("¿Qué letra estará en esta palabra misteriosa?:");
        char c = scan.next().charAt(0);
        hangMan.tryChar(c);
        hangMan.showHidenWord();

    }

}
