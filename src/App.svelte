<script>
  import {Route, Router} from "svelte-routing";
  import Home from "./routes/Home.svelte";
  import Register from "./routes/Register.svelte";
</script>

<Router>
  <Route path="/" component={Home} />
  <Route path="register" component={Register} />
</Router>
