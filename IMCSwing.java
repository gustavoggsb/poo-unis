import javax.swing.JOptionPane;
import java.text.DecimalFormat;

/**
 *
 * @author Gustavo Baptista
 */

public class IMCSwing {
  public static void main(String[] args) {
    String name;
    float weight, height;
    float imc;
    String result;

    name = JOptionPane.showInputDialog("Me diga o seu nome?");
    weight = Float.parseFloat(JOptionPane.showInputDialog("Me diga agora seu Peso em Kg: (Exemplo: 62.8)"));
    height = Float
        .parseFloat(JOptionPane.showInputDialog("Por fim, me diga qual sua altura em metros: (Exemplo: 1.85)"));

    imc = (float) (weight / Math.pow(height, 2));
    if (imc <= 17)
      result = "Muito abaixo do peso";
    else if (imc >= 17 && imc <= 18.49)
      result = "Abaixo do Peso";
    else if (imc >= 18.50 && imc <= 24.99)
      result = "Peso normal";
    else if (imc >= 25 && imc <= 29.99)
      result = "Obesidade I";
    else if (imc >= 30 && imc <= 34.99)
      result = "Obesidade II";
    else
      result = "Obesidade mórbida! Procure urgenteente um médico.";

    DecimalFormat formater = new DecimalFormat("##.##");

    JOptionPane.showMessageDialog(null, "Olá, " + name + " seu resultado é: " + formater.format(imc) + " > " + result);
  }
}
