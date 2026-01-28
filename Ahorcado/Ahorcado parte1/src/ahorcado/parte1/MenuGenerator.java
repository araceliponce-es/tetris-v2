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

    private HangMan hangMan;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        MenuGenerator menuGenerator = new MenuGenerator();
        do {
            menuGenerator.hangMan = new HangMan(menuGenerator.showInitMenu());
            menuGenerator.showGameMenu();
            if(menuGenerator.hangMan.isGameOver() && menuGenerator.hangMan.maxFailsExceeded()){
                System.out.println("Perdiste, la palabra era: "+menuGenerator.hangMan.showFullWord());
            }else if(menuGenerator.hangMan.isGameOver()){
                System.out.println("Ganaste, la palabra era: "+menuGenerator.hangMan.showFullWord());
            }
        } while (!menuGenerator.showExitMenu());
        

    }

    private String showInitMenu() {
        WordGenerator palabraSecr = new WordGenerator();
        return palabraSecr.generateWord();
    }

    private void showGameMenu() {
        Scanner scan = new Scanner(System.in);
        while (!hangMan.isGameOver()) {
            
            System.out.println("¿Qué letra estará en esta palabra misteriosa?:");
            System.out.println("");
            char c = scan.next().charAt(0);
            hangMan.tryChar(c);
            System.out.println();
            System.out.println(hangMan.showHidenWord());
            System.out.println("Letras falladas: "+hangMan.getStringFails());
        }

    }

    private boolean showExitMenu() {
        if (hangMan.isGameOver()) {
            System.out.println("¿Quieres jugar otra vez?(s/n)");
            Scanner scan = new Scanner(System.in);
            String respuesta = scan.nextLine();
            return !("s".equalsIgnoreCase(respuesta));
        } else {
            return false;
        }
    }

}
