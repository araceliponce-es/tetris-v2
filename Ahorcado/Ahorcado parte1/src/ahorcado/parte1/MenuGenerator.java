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
        
        do{
        menuGenerator.hangMan = new HangMan(menuGenerator.showInitMenu());
        menuGenerator.showGameMenu();
        }while(!menuGenerator.showExitMenu());

    }

    private String showInitMenu() {
        WordGenerator palabraSecr = new WordGenerator();
        return palabraSecr.generateWord();
    }

    private void showGameMenu() {
        Scanner scan = new Scanner(System.in);
        while(!hangMan.maxFailsExceeded()){
        System.out.println(hangMan.getStringFails());
        System.out.println("¿Qué letra estará en esta palabra misteriosa?:");
        char c = scan.next().charAt(0);
        hangMan.tryChar(c);
        System.out.println(hangMan.showHidenWord());
        }

    }
    
    private boolean showExitMenu(){
        if(hangMan.maxFailsExceeded() || hangMan.isGameOver() ){
        System.out.println("¿Quieres jugar otra vez?(s/n)");
        Scanner scan = new Scanner(System.in);
        String respuesta = scan.nextLine();
        return !("s".equals(respuesta) || "S".equals(respuesta));
        }else{
            return false;
        }
    }

}
