Kaavio sovelluslogiikan luokista ja niiden suhteista toisiinsa:

```mermaid
 classDiagram
      SignUp --> Login
      Login --> SignUp
      Login --> CalculatorLogic
      CalculatorLogic --> Login
      CalculatorLogic --> FetchHistory
      FetchHistory --> CalculatorLogic
      class SignUp{
      }
      class Login{
      }
      class CalculatorLogic{
      }
      
```
