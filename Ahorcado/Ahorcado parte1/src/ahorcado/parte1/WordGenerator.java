/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ahorcado.parte1;

/**
 *
 * @author Araceli,Diego,Óscar
 */
public class WordGenerator {

    private String[] seleccionPalabras = new String[5];

    public String generateWord() {
        seleccionPalabras[0]="Guacamole";
        seleccionPalabras[1]="Aguacate";
        seleccionPalabras[2]="Cilantro";
        seleccionPalabras[3]="Jalapeño";
        seleccionPalabras[4]="Cebolla";
        int escogida = new java.util.Random().nextInt(5);
        String palabra=seleccionPalabras[escogida];
        return palabra;
    }

}
